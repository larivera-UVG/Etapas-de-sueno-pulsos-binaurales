%% Entrenamiento de modelo SVM, usando distintos tipos de Kernel
%  Nota: El entrenamiento y la validación cruzada pueden tomar algún tiempo.

X = [Datos{1};Datos{2};Datos{3};Datos{4};Datos{5}];  % Todos los datos juntos
half = floor(length(X)/2);
X_Train = X(1:half,:);
% Las etiquetas son números enteros, distintos para cada clase. Podrían usarse otro tipo
% de etiquetas.
Etiquetas = grp2idx(hypnogram);
% Etiquetas = [ones(size(Datos{1},1),1); 2*ones(size(Datos{2},1),1); 3*ones(size(Datos{3},1),1);4*ones(size(Datos{4},1),1);5*ones(size(Datos{5},1),1)];
half2 = floor(length(Etiquetas)/2);
E_Train = Etiquetas(1:half2);
% Primero se escoge el tipo de Kernel
tipo_Kernel = 1; % 0 - Gaussiano, 1 - Lineal, 2 - Polinom. grado 2, 3 - Polinom. grado 3

switch tipo_Kernel 
    case 0
        plantilla = templateSVM('KernelFunction', 'gaussian');
        
    case 1
        plantilla = templateSVM('KernelFunction', 'linear');
        
    case 2
        plantilla = templateSVM('KernelFunction', 'polynomial', 'PolynomialOrder', 2);
        
    case 3
        plantilla = templateSVM('KernelFunction', 'polynomial', 'PolynomialOrder', 3);
end
options = statset('UseParallel',true);
Mdl = fitcecoc(X, Etiquetas, 'Learners', plantilla, 'Verbose', 2,'Options',options);

% Validación cruzada
CVMdl = crossval(Mdl);

% Porcentaje de error de clasificación (promedio de la validación cruzada).
genError = 100*kfoldLoss(CVMdl)

oofLabel = kfoldPredict(CVMdl,'Options',options);
%% Clasificación de muestras nuevas, no usadas antes
% Xtest = [5,-1,0;2,-1,2;3,1,5];  % 3 muestras (vectores fila)
%  Xtest = X(half+2:end,:);
%  EK = Etiquetas(half+2:end,:);
% Clasif_test = predict(Mdl,Xtest);
% [cm,order] = confusionmat(EK,Mdl);
MsC = confusionchart(Etiquetas,oofLabel,'RowSummary','total-normalized');
% Clasif_test = predict(Mdl,X);
% [cm,order] = confusionmat(Etiquetas',Clasif_test');
% plotconfusion(Etiquetas(half+2:end,:)',Clasif_test');