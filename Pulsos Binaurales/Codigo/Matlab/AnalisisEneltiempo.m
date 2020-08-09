%Leemos el archivo wav generado por el programa
[y,fs] = audioread('Binaural0.wav');
%Se verifica si hay un sonido estére (Buscamos N = 2)
[M,N] = size(y);
%Separamos ambos canales
left_channel = y(:,1);
right_channel = y(:,2);
%Definimos el pulso binaural que se interpretaría 
binaural_beat= right_channel-left_channel;
%Se hace un ajuste para tener la referencia en segundos
t= (0:441000-1) / fs;
plot(t,binaural_beat);
title('Pulso binaural');
 xlabel('Tiempo (s)')
 ylabel('Amplitud')
