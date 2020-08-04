%Leemos el archivo wav generado por el programa
[y,fs] = audioread('Binaural0.wav');
%Se verifica si hay un sonido estére (Buscamos N = 2)
[M,N] = size(y);
%Separamos ambos canales
left_channel = y(:,1);
right_channel = y(:,2);
%Definimos el pulso binaural que se interpretaría 
binaural_beat= right_channel-left_channel;
Fs = 44100;                    % Sampling frequency
T = 1/Fs;                     % Sample time
L = length(y);                     % Length of signal
t = (0:L-1)*T;                % Time vector
NFFT = 2^nextpow2(L); % Next power of 2 from length of y
Y = fft(binaural_beat,NFFT)/L;
f = Fs/2*linspace(0,1,NFFT/2+1);

% Plot single-sided amplitude spectrum.
plot(f,2*abs(Y(1:NFFT/2+1))) 
title('Análisis de Espectro de frecuencias Pulso Binaural')
xlabel('Frecuencia (Hz)')
ylabel('|Y(f)|')