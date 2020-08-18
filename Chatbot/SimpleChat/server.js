var express = require('express');
var app = express();
var cfenv = require('cfenv');
var appEnv = cfenv.getAppEnv();
var port = process.env.PORT || 8098;

app.use(express.static(__dirname+'/public'));

app.use(function(req, res, next) 
{
	    res.header("Access-Control-Allow-Origin", "*");
		res.header("Access-Control-Allow-Headers", "X-Requested-With,Content-Type");
		res.header('Access-Control-Allow-Methods','GET,POST');
	    res.setHeader('Content-Type', 'application/json');
	    console.log("Server initialization .. ");
	    next();
});

app.listen(port);
console.log("App listening on port " + port);