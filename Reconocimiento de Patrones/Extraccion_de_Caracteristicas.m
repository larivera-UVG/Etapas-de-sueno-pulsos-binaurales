
%Seleccionar que grabación se quiere utilizar
load('data_1')

% Extracción de señales
numEp = length(hypnogram);
L = 3000;   % longitud de las epochs (número de muestras)
Raw_seccionado = zeros(L,numEp);

% Extraer las épocas de la señal entera
for n = 1:numEp
    Raw_seccionado(:,n) = fpz(((n-1)*L+1):n*L);
end

Labels = hypnogram';

W = 300; % Número de señales de la clase WAKE (si no se sabe, dar un número que alcance)
S1 = 300; % Número de señales de la clase 2
S2 = 400; % Número de señales de la clase 2 
S3 = 500; % Número de señales de la clase 3 
S4 = 300; % Número de señales de la clase 4
REM = 300; % Número de señales de la clase REM

Raw_W = zeros(L,W);
Raw_S1 = zeros(L,S1);
Raw_S2 = zeros(L,S2);
Raw_S3 = zeros(L,S3);
Raw_S4 = zeros(L,S4);
Raw_REM = zeros(L,REM);

cont_W = 0;
cont_S1 = 0;
cont_S2= 0;
cont_S3 = 0;
cont_S4 = 0;
cont_REM = 0;

for n = 1:numEp
    if(Labels(n) == 'W')
        cont_W = cont_W + 1;
        Raw_W(:,cont_W) = Raw_seccionado(:,n);

    elseif(Labels(n) == '1')
        cont_S1 = cont_S1 + 1;
        Raw_S1(:,cont_S1) = Raw_seccionado(:,n);

    elseif(Labels(n) == '2')
        cont_S2 = cont_S2 + 1;
        Raw_S2(:,cont_S2) = Raw_seccionado(:,n);

    elseif(Labels(n) == '3')
        cont_S3 = cont_S3 + 1;
        Raw_S3(:,cont_S3) = Raw_seccionado(:,n);
      
    elseif(Labels(n) == '4')
        cont_S4 = cont_S4 + 1;
        Raw_S4(:,cont_S4) = Raw_seccionado(:,n);
   
    else
        cont_REM = cont_REM + 1;
        Raw_REM(:,cont_REM) = Raw_seccionado(:,n);
    end
end

% Remover las columnas que sobraron
Raw_W = Raw_W(:,1:cont_W);
Raw_S1 = Raw_S1(:,1:cont_S1);
Raw_S2 = Raw_S2(:,1:cont_S2);
Raw_S3 = Raw_S3(:,1:cont_S3);
Raw_S4 = Raw_S4(:,1:cont_S4);
Raw_REM = Raw_REM(:,1:cont_REM);


%% Extracción de características
WAKE = zeros(cont_W,2);
STAGE_1 = zeros(cont_S1,2);
STAGE_2 = zeros(cont_S2,2);
STAGE_3 = zeros(cont_S3,2);

REM = zeros(cont_REM,2);

Target_Wake = zeros(5,cont_W);
Target_S1 = zeros(5,cont_S1);
Target_S2 = zeros(5,cont_S2);
Target_S3 = zeros(5,cont_S3);
Target_S4 = zeros(5,cont_S4);
Target_REM = zeros(5,cont_REM);

%% Características
% Modificar funciones de extracción según se requiera
for n = 1:cont_W
    WAKE(n,1) = mean(abs(Raw_W(:,n)));
    WAKE(n,2) = ZC_v2(Raw_W(:,n),0.01);
    WAKE(n,3) = MMD(Raw_W(:,n));
    Target_Wake(:,n) = [1;0;0;0;0];
end

for n = 1:cont_S1
    STAGE_1(n,1) = mean(abs(Raw_S1(:,n)));
    STAGE_1(n,2) = ZC_v2(Raw_S1(:,n),0.01);
    STAGE_1(n,3) = MMD(Raw_S1(:,n));
    Target_S1(:,n) = [0;1;0;0;0];
end

for n = 1:cont_S2
    STAGE_2(n,1) = mean(abs(Raw_S2(:,n)));
    STAGE_2(n,2) = ZC_v2(Raw_S2(:,n),0.01);
    STAGE_2(n,3) = MMD(Raw_S2(:,n));

    Target_S2(:,n) = [0;0;1;0;0];
end

for n = 1:cont_S3
    STAGE_3(n,1) = mean(abs(Raw_S3(:,n)));
    STAGE_3(n,2) = ZC_v2(Raw_S3(:,n),0.01);
    STAGE_3(n,3) = MMD(Raw_S3(:,n));

    Target_S3(:,n) = [0;0;0;1;0];
end

for n = 1:cont_REM
    REM(n,1) = mean(abs(Raw_REM(:,n)));
    REM(n,2) = ZC_v2(Raw_REM(:,n),0.01);
    REM(n,3) = MMD(Raw_REM(:,n));
    Target_REM(:,n) = [0;0;0;0;1];
end

c = 4;
Datos = cell(1,c);
Datos{1,1} = WAKE;
Datos{1,2} = STAGE_1;
Datos{1,3} = STAGE_2;
Datos{1,4} = STAGE_3;
Datos{1,5} = REM;

%% Crear Target e Input Vector
numF = 2;
numCl = 5;
numEp2 = numEp - cont_REM;
Input_Vector = zeros(numF,numEp2);
Target_Vector = zeros(numCl,numEp2);

WAKE=WAKE';
STAGE_1=STAGE_1';
STAGE_2=STAGE_2';
STAGE_3=STAGE_3';
REM=REM';

%Wake
Input_Vector(:,1:cont_W)= WAKE(1:numF,:);
Target_Vector(:,1:cont_W) = Target_Wake;

%Stage_1
Input_Vector(:,cont_W+1:cont_W+cont_S1)= STAGE_1(1:numF,:);
Target_Vector(:,cont_W+1:cont_W+cont_S1) = Target_S1;

%Stage_2
Input_Vector(:,cont_W+cont_S1+1:cont_W+cont_S1+cont_S2)= STAGE_2(1:numF,:);
Target_Vector(:,cont_W+cont_S1+1:cont_W+cont_S1+cont_S2) = Target_S2;

%Stage_3
Input_Vector(:,cont_W+cont_S1+cont_S2+1:cont_W+cont_S1+cont_S2+cont_S3)= STAGE_3(1:numF,:);
Target_Vector(:,cont_W+cont_S1+cont_S2+1:cont_W+cont_S1+cont_S2+cont_S3) = Target_S3;

%REM
Input_Vector(:,cont_W+cont_S1+cont_S2+cont_S3+1:cont_W+cont_S1+cont_S2+cont_S3+cont_REM)= REM(1:numF,:);
Target_Vector(:,cont_W+cont_S1+cont_S2+cont_S3+1:cont_W+cont_S1+cont_S2+cont_S3+cont_REM) = Target_REM;

