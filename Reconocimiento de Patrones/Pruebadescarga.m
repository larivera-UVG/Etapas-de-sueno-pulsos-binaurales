[saved_file, status] = downloadEDFxData();
downloadEDFxAnnotations( );
convertEDFxToMat(saved_file{5}, status{5});
hypnogram = processEDFxHypnogram(saved_file{5});
