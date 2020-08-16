clear all;

%%  Establecer la longitud de las epocas que se desea e inicializacion de variables
Epocas_Length = 30; % Duracion en segundos de cada epoca
Canales = 8;        % Numero de canales que se desea usar (1 a 8)
itr = 1;
t=1:1000;
vproyecto = zeros(1000,8);
i = 1;
ctrl = 0;
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
Live_Data1 = zeros(Row,Col);
Temp_Raw_Vector = zeros(Epocas_Length*100,8);
Live_Data_test = [];
Live_Data_test2 = [];
Full_Fill_Vec = [];
Proseced_Data = [];
Feature_1 = [];
Feature_2 = [];
Feature_3 = [];
Feature_4 = [];
Feature_5 = [];
Feature1_Vec = [];
Feature2_Vec = [];
Feature3_Vec = [];
Feature4_Vec = [];
Feature5_Vec = [];
Feature6_Vec = [];
Feature7_Vec = [];
Feature8_Vec = [];
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

cont = 1;
cont2 = Epocas_Length*250;
while ctrl<=50
    
    Epoc = [];
    [vec,ts] = inlet.pull_sample(); % Se realiza la lectura de los 8 canales 
    Live_Data_test2 = cat(1,Live_Data_test2,vec); % Cada lectura se almacena 
    
    display_buff_filt = filter(b2,a2,Live_Data_test2); % Se realiza el friltrado del los datos
    display_buff_filt = filter(b,a,display_buff_filt);
    
    i=i+1;
    if(mod(i,Epocas_Length*250)==0) % Cada vez que pase cierta cantidad de tiempo se hace la separacion de epocas
        i=1;
        Pre_Epoc = display_buff_filt(cont:end ,:);
        cont = cont + cont2;
        Epoc = cat(1,Epoc,Pre_Epoc); 
        flag = true;    % cuando se cumpla esta condicion se levanta una bandera para poder sacarle las caracterisiticas a dicha epoca
    else
        flag = false;
    end
   
    
    if flag == true
        %Extraer caracteristicas
        Chn1 = Epoc(: , 1);
        Chn2 = Epoc(: , 2);
        Chn3 = Epoc(: , 3);
        Chn4 = Epoc(: , 4);
        Chn5 = Epoc(: , 5);
        Chn6 = Epoc(: , 6);
        Chn7 = Epoc(: , 7);
        Chn8 = Epoc(: , 8);
        
        clear Epoc;
        
        Feature_1 = [mean(abs(Chn1)),mean(abs(Chn2)),mean(abs(Chn3)),mean(abs(Chn4)),mean(abs(Chn5)),mean(abs(Chn6)),mean(abs(Chn7)),mean(abs(Chn8))];
        Feature_2 = [Zero_Crossing(Chn1,0.01),Zero_Crossing(Chn2,0.01),Zero_Crossing(Chn3,0.01),Zero_Crossing(Chn4,0.01),Zero_Crossing(Chn5,0.01),Zero_Crossing(Chn6,0.01),Zero_Crossing(Chn7,0.01),Zero_Crossing(Chn8,0.01)];
        Feature_3 = [Min_Max_Distance(Chn1),Min_Max_Distance(Chn2),Min_Max_Distance(Chn3),Min_Max_Distance(Chn4),Min_Max_Distance(Chn5),Min_Max_Distance(Chn6),Min_Max_Distance(Chn7),Min_Max_Distance(Chn8)];
        Feature_4 = [bandpower(Chn1),bandpower(Chn2),bandpower(Chn3),bandpower(Chn4),bandpower(Chn5),bandpower(Chn6),bandpower(Chn7),bandpower(Chn8)];
        Feature_5 = [kurtosis(Chn1),kurtosis(Chn2),kurtosis(Chn3),kurtosis(Chn4),kurtosis(Chn5),kurtosis(Chn6),kurtosis(Chn7),kurtosis(Chn8)];
        
        % Cada caracteristica se almacena en vectores diferentes a medida
        % que se extraen
        Feature1_Vec = cat(1,Feature1_Vec,Feature_1);
        Feature2_Vec = cat(1,Feature2_Vec,Feature_2);
        Feature3_Vec = cat(1,Feature3_Vec,Feature_3);
        Feature4_Vec = cat(1,Feature4_Vec,Feature_4);
        Feature5_Vec = cat(1,Feature5_Vec,Feature_5);
        
        itr = 0;
        disp('Done');
        ctrl = ctrl + 1; % variable de control de duracion de la simulacion 
    end
end