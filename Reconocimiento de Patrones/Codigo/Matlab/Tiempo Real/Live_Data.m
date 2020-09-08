clear all;

%%  Establecer la longitud de las epocas que se desea e inicializacion de variables
Epocas_Length = 30; % Duracion en segundos de cada epoca
Canales = 8;        % Numero de canales que se desea usar (1 a 8)
itr = 1;
t=1:1000;
vproyecto = zeros(1000,8);
i = 1;
ctrl = 0;
ctrl2 = 1;
M = 2;
%% Se definen los parametros para los filtros
fs_Hz = 250;
little_buff = zeros(1,10);
display_buff = zeros(1,5000);
cont = 1;

bpf = [5, 50];
[b,a] = butter(2,bpf/(fs_Hz / 2), 'bandpass');

notch = [59, 61];
[b2, a2] = butter(2,notch/(fs_Hz / 2), 'stop');

%%  Reservar memoria para vector de datos raw y para filtrar los datos
Col = 8;
Row = 50000000;
Offset = zeros(1,8);
Live_Data1 = zeros(Row,Col);
Live_Data_test = [];
Feature1_Vec = zeros(M,8);
Feature2_Vec = zeros(M,8);
Feature3_Vec = zeros(M,8);
Feature4_Vec = zeros(M,8);
Feature5_Vec = zeros(M,8);
Live_Data_test2 = zeros(Epocas_Length*250,8);
Fixed_Vector = zeros(Epocas_Length*250,8);
Full_Fill_Vec = zeros(2*Epocas_Length*250,8);
Temp_Raw_Vector = zeros(2*Epocas_Length*100,8);
index1 = 1;
cont = 1;
cont2 = Epocas_Length*250;
cont3 = Epocas_Length*250;
tiempos = zeros(Epocas_Length*250,1);
%% instantiate the library
disp('Loading the library...');
lib = lsl_loadlib();
% resolve a stream...
disp('Resolving an EEG stream...');
result = {};
while isempty(result)
    result = lsl_resolve_byprop(lib,'type','EEG');
end

% create a new inlet
disp('Opening an inlet...');
inlet = lsl_inlet(result{1});
disp('Now receiving data...');


mitimer  = tic;
n = 1;


while true
    
    [vec,ts] = inlet.pull_sample();                         % Se realiza la lectura de los 8 canales 
    tiempos(n) = toc(mitimer);
    mitimer  = tic;
    n = n +1;
    Live_Data_test2(index1,:) =  vec;                       % Se ingresa los datos leidos a un vector temporal
    
    i=i+1;
    if(mod(i,Epocas_Length*250+1)==0)                       % Cada vez que pase cierta cantidad de tiempo se hace la separacion de epocas
        i=1;
        if (min(Live_Data_test2)==0)
             [M,I] = find(Live_Data_test2 == 0);
             Live_Data_test2(M,I) = Offset;
             fprintf('/');
        end
        Fixed_Vector = Live_Data_test2 - (Offset);
%         Fixed_Vector = Live_Data_test2 - Live_Data_test2(1,:);
        display_buff_filt = filter(b2,a2,Fixed_Vector);  % Se realiza el friltrado del los datos
        display_buff_filt = filter(b,a,display_buff_filt);
        Offset = [mean(Live_Data_test2(:,1)),mean(Live_Data_test2(:,2)),mean(Live_Data_test2(:,3)),mean(Live_Data_test2(:,4)),mean(Live_Data_test2(:,5)),mean(Live_Data_test2(:,6)),mean(Live_Data_test2(:,7)),mean(Live_Data_test2(:,8))];
%         Offseet = mean(Live_Data_test2,1);
        Full_Fill_Vec(cont:cont3 ,:) = Live_Data_test2;     % Se almacenan los datos de cada epoca de los valores en bruto
        Temp_Raw_Vector(cont:cont3,:) = display_buff_filt;  % Se almacenan los datos de cada epoca de los valores filtrados
        cont = cont + cont2;                                % Contador para la primera posicion de la proxima epoca a guardar
        cont3 = cont3 + cont2;                              % Contador de la ultima posicion de la proxima epoca a guardar
        index1 = 1;
        flag = true;                                        % cuando se cumpla esta condicion se levanta una bandera para poder sacarle las caracterisiticas a dicha epoca
    else
        flag = false;
        index1 = index1 + 1;
    end
   
    
    if flag == true
        %Extraer caracteristicas
        Chn1 = display_buff_filt(: , 1);
        Chn2 = display_buff_filt(: , 2);
        Chn3 = display_buff_filt(: , 3);
        Chn4 = display_buff_filt(: , 4);
        Chn5 = display_buff_filt(: , 5);
        Chn6 = display_buff_filt(: , 6);
        Chn7 = display_buff_filt(: , 7);
        Chn8 = display_buff_filt(: , 8);
        
        
        Feature1_Vec(ctrl2,:) = [mean(abs(Chn1)),mean(abs(Chn2)),mean(abs(Chn3)),mean(abs(Chn4)),mean(abs(Chn5)),mean(abs(Chn6)),mean(abs(Chn7)),mean(abs(Chn8))];
        Feature2_Vec(ctrl2,:) = [Zero_Crossing(Chn1,0.01),Zero_Crossing(Chn2,0.01),Zero_Crossing(Chn3,0.01),Zero_Crossing(Chn4,0.01),Zero_Crossing(Chn5,0.01),Zero_Crossing(Chn6,0.01),Zero_Crossing(Chn7,0.01),Zero_Crossing(Chn8,0.01)];
        Feature3_Vec(ctrl2,:) = [Min_Max_Distance(Chn1),Min_Max_Distance(Chn2),Min_Max_Distance(Chn3),Min_Max_Distance(Chn4),Min_Max_Distance(Chn5),Min_Max_Distance(Chn6),Min_Max_Distance(Chn7),Min_Max_Distance(Chn8)];
        Feature4_Vec(ctrl2,:) = [bandpower(Chn1),bandpower(Chn2),bandpower(Chn3),bandpower(Chn4),bandpower(Chn5),bandpower(Chn6),bandpower(Chn7),bandpower(Chn8)];
        Feature5_Vec(ctrl2,:) = [kurtosis(Chn1),kurtosis(Chn2),kurtosis(Chn3),kurtosis(Chn4),kurtosis(Chn5),kurtosis(Chn6),kurtosis(Chn7),kurtosis(Chn8)];
        
        itr = 0;
        fprintf('Done - %d \n',ctrl);
        ctrl = ctrl + 1; % variable de control de duracion de la simulacion 
        ctrl2 = ctrl2 + 1;
    end
end