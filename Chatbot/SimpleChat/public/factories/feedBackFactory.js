webinarApp.factory('feedBackFactory', function($http,urlMapperService) {
	var getFeedBackDetails= function(param) {
		var url = urlMapperService.getUrl('feedbackURL');		
		var targetUrl = url + 'emailid='+param.emailid 
	    return $http.get(targetUrl);
	  };
  return {
	  getFeedBackDetails: getFeedBackDetails
	  
  };
	
	
  
});
webinarApp.factory('feedBack', function($http,urlMapperService) {
	var getFeedBack= function() {
		var url = urlMapperService.getUrl('feedbackURL');		
		var targetUrl = url + 'emailid='+"sakshichandni@gmail.com"
	    return $http.get(targetUrl);
	  };
  return {
	  getFeedBack: getFeedBack
	  
  };
	
	
  
});

