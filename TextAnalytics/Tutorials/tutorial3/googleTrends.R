##### Import Google Trends Data
 print(getwd())

 google = read.csv('IPHONE.csv');
 google$date = as.Date(google$date); 
 
 ##### Sales Data 
 dat = read.csv("IPHONE.csv"); 
 dat$month = as.Date(dat$date); 
 
 
 
 ##### get ready for the forecasting; 
 dat = rbind(dat, dat[nrow(dat), ]); 
 dat[nrow(dat), ’month’] = as.Date(’2008-09-01’); 
 dat[nrow(dat), -1] = rep(NA, ncol(dat)-1); 