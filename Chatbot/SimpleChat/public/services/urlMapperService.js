webinarApp.service('urlMapperService', function(){
    this.urlMapper = {};
    this.urlMapper.feedbackURL = "http://hidemo.cloudapp.net:8004/getFeedback?";
    this.urlMapper.updateDBUrl="http://paymentmod.cloudapp.net:8060/updateDB/"
    this.urlMapper.updateStatusUrl="http://raas-dev.cloudapp.net:6010/api/v1.0/godrej/changeJobStatus"
	this.getUrl =function(url){
		return this.urlMapper[url];
	};
});