%%  Establecer la longitud de las epocas que se desea e inicializacion de variables
Epocas_Length = 30; % Duracion en segundos de cada epoca
Canales = 8;        % Numero de canales que se desea usar (1 a 8)
itr = 1;
t=1:1000;
vproyecto = zeros(1000,8);
i = 1;
ctrl = 0;
%%  Reservar memoria para vector de datos raw y para filtrar los datos
Col = 8;
Row = 50000000;
Live_Data = zeros(Row,Col);
Temp_Raw_Vector = zeros(Epocas_Length*100,8);
Live_Data_test = [];
Live_Data_test2 = [];
Full_Fill_Vec = [];
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

% figure('Name', 'Lecturas')
% grafica = plot(t, vproyecto);
% title('EEG');
% xlabel('T (s)');
% ylabel('Señal (V)');
% % ylim([-5 5]);
% grid on;
% hold on;

while true
    
    
    [vec,ts] = inlet.pull_sample();
    vproyecto(i,:) = vec;
    Live_Data_test2 = cat(1,Live_Data_test2,vec);
    %      grafica.YData(i) = vproyecto(i,1);
    %     drawnow limitrate
    
    i=i+1;
    if(mod(i,1001)==0)
        i=1;
        Live_Data_test = cat(1,Live_Data_test,vproyecto); % todos los datos Raw obtenidos de la cyton
        flag = true;
    end
    
    fs_Hz = 250;
    little_buff = zeros(1,10);
    display_buff = zeros(1,5000);
    cont = 1;
    
    bpf = [5, 50];
    [b,a] = butter(2,bpf/(fs_Hz / 2), 'bandpass');
    
    notch = [59, 61];
    [b2, a2] = butter(2,notch/(fs_Hz / 2), 'stop');
    
    if flag == true
        display_buff_filt = filter(b2,a2,Live_Data_test);
        display_buff_filt = filter(b,a,display_buff_filt);
        
        %Extraer caracteristicas
        Chn1 = display_buff_filt(: , 1);
        Chn2 = display_buff_filt(: , 2);
        Chn3 = display_buff_filt(: , 3);
        Chn4 = display_buff_filt(: , 4);
        Chn5 = display_buff_filt(: , 5);
        Chn6 = display_buff_filt(: , 6);
        Chn7 = display_buff_filt(: , 7);
        Chn8 = display_buff_filt(: , 8);
        Chn_Combine = [Chn1;Chn2;Chn3;Chn4;Chn5;Chn6;Chn7;Chn8];
        
        if itr == Epocas_Length*250
            Feature_1 = [mean(abs(Chn1)),mean(abs(Chn2)),mean(abs(Chn3)),mean(abs(Chn4)),mean(abs(Chn5)),mean(abs(Chn6)),mean(abs(Chn7)),mean(abs(Chn8))];
            Feature_2 = [Zero_Crossing(Chn1,0.01),Zero_Crossing(Chn2,0.01),Zero_Crossing(Chn3,0.01),Zero_Crossing(Chn4,0.01),Zero_Crossing(Chn5,0.01),Zero_Crossing(Chn6,0.01),Zero_Crossing(Chn7,0.01),Zero_Crossing(Chn8,0.01)];
            Feature_3 = [Min_Max_Distance(Chn1),Min_Max_Distance(Chn2),Min_Max_Distance(Chn3),Min_Max_Distance(Chn4),Min_Max_Distance(Chn5),Min_Max_Distance(Chn6),Min_Max_Distance(Chn7),Min_Max_Distance(Chn8)];
            Feature_4 = [bandpower(Chn1),bandpower(Chn2),bandpower(Chn3),bandpower(Chn4),bandpower(Chn5),bandpower(Chn6),bandpower(Chn7),bandpower(Chn8)];
            Feature_5 = [kurtosis(Chn1),kurtosis(Chn2),kurtosis(Chn3),kurtosis(Chn4),kurtosis(Chn5),kurtosis(Chn6),kurtosis(Chn7),kurtosis(Chn8)];
            
            Conv_F1 = [Feature_1(1);Feature_1(2);Feature_1(3);Feature_1(4);Feature_1(5)];
            Conv_F2 = [Feature_2(1);Feature_2(2);Feature_2(3);Feature_2(4);Feature_2(5)];
            Conv_F3 = [Feature_3(1);Feature_3(2);Feature_3(3);Feature_3(4);Feature_3(5)];
            Conv_F4 = [Feature_4(1);Feature_4(2);Feature_4(3);Feature_4(4);Feature_4(5)];
            Conv_F5 = [Feature_5(1);Feature_5(2);Feature_5(3);Feature_5(4);Feature_5(5)];
           
            
            Feature1_Vec = cat(1,Feature1_Vec,Conv_F1);
            Feature2_Vec = cat(1,Feature2_Vec,Conv_F2);
            Feature3_Vec = cat(1,Feature3_Vec,Conv_F3);
            Feature4_Vec = cat(1,Feature4_Vec,Conv_F4);
            Feature5_Vec = cat(1,Feature5_Vec,Conv_F5);
            
%             FVC = [Feature_1',Feature_2',Feature_3',Feature_4',Feature_5',Feature_1',Feature_2',Feature_3',Feature_4',Feature_5',Feature_1',Feature_2',Feature_3',Feature_4',Feature_5',Feature_5'];
            itr = 0;
            Str = "Done"
            
%             Clasif_test = predict(Mdl,FVC)
            ctrl = ctrl + 1;
        else
            itr = itr + 1;
            
        end
    end
    
    %     fprintf('%.2f\t',vec);
    %     fprintf('%.5f\n',ts);
end