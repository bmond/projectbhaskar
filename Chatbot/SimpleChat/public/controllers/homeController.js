  webinarApp.controller('homeController',['$scope','$window','$location','$anchorScroll',
  '$stateParams','$state','$filter','$q','$timeout','feedBackFactory','$http',
   function($scope,$window,
    $location, $anchorScroll,$stateParams,
    $state,$filter,$q,$timeout,feedBackFactory,$http) { 
      $(function() {
    var INDEX = 0; 
    $("#chat-submit").click(function(e) {
      e.preventDefault();
      var msg = $("#chat-input").val(); 
      //var msg = 'Hello';
      if(msg.trim() == ''){
        return false;
      }
      generate_message(msg, 'self');
      var buttons = [
          {
            name: 'Existing User',
            value: 'existing'
          },
          {
            name: 'New User',
            value: 'new'
          }
        ];
      setTimeout(function() {      
        generate_message(msg, 'user');  
      }, 1000)
      
    })
    
    function generate_message(msg, type) {
      INDEX++;
      var str="";
      
      if (type == 'self'){
        str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
      str += "          <span class=\"msg-avatar\">";
      str += "            <img src=\"https:\/\/image.crisp.im\/avatar\/operator\/196af8cc-f6ad-4ef7-afd1-c45d5231387c\/240\/?1483361727745\">";
      str += "          <\/span>";
      str += "          <div class=\"cm-msg-text\">";
        str += msg;
        str += "          <\/div>";
      str += "        <\/div>";
      $(".chat-logs").append(str);
      $("#cm-msg-"+INDEX).hide().fadeIn(300);
      if(type == 'self'){
       $("#chat-input").val(''); 
      }    
      $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000); 
      } else {
        console.log('okkk');
        //alert('it is coming to else');

        $http({

                          method : 'Post',
                          url : 'http://paymentmod.cloudapp.net:8000/digitalOnboardingFedSearch/',
                          //headers: {'Content-Type': application/x-www-form-urlencoded},mimeType: 'multipart/form-data',
                          
                          headers: { 'Content-Type': 'application/x-www-form-urlencoded'},
                          //'Access-Control-Allow-Origin':'*',
                          //'Access-Control-Allow-Methods':'*'},
                          
                          data: { "query": msg, "user":"hmsakshikavya@gmail.com","channel":"dcob", "language":"en"}
                          //alert('ajsakjd');
                      }).then(function successCallback(response) {
                        console.log(response.data.payload);
                        str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
      str += "          <span class=\"msg-avatar\">";
      str += "            <img src=\"\.\.\/templates\/images\/profile-pic.jpg\">";
      str += "          <\/span>";
      str += "          <div class=\"cm-msg-text\">";
                          
                          str+=response.data.payload;
                          str += "          <\/div>";
      str += "        <\/div>";
      $(".chat-logs").append(str);
      $("#cm-msg-"+INDEX).hide().fadeIn(300);
      if(type == 'self'){
       $("#chat-input").val(''); 
      }    
      $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000); 
                          console.log(str);

                      }, function errorCallback(err,response) {
                        str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
      //str += "          <span class=\"msg-avatar\">";
      //str += "            <img src=\"\.\.\/templates\/images\/profile-pic.jpg\">";
      //str += "          <\/span>";
      str += "          <div >";
                          
                          str+='Some network problem. Please try later.';
                          str += "          <\/div>";
      str += "        <\/div>";
      $(".chat-logs").append(str);
      $("#cm-msg-"+INDEX).hide().fadeIn(300);
      if(type == 'self'){
       $("#chat-input").val(''); 
      }    
      $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000); 

                          
                      });
      }
      
      
         
    }  
    
    function generate_button_message(msg, buttons){    
      /* Buttons should be object array 
        [
          {
            name: 'Existing User',
            value: 'existing'
          },
          {
            name: 'New User',
            value: 'new'
          }
        ]
      */
      INDEX++;
      var btn_obj = buttons.map(function(button) {
         return  "              <li class=\"button\"><a href=\"javascript:;\" class=\"btn btn-primary chat-btn\" chat-value=\""+button.value+"\">"+button.name+"<\/a><\/li>";
      }).join('');
      var str="";
      str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg user\">";
      str += "          <span class=\"msg-avatar\">";
      str += "            <img src=\"https:\/\/image.crisp.im\/avatar\/operator\/196af8cc-f6ad-4ef7-afd1-c45d5231387c\/240\/?1483361727745\">";
      str += "          <\/span>";
      str += "          <div class=\"cm-msg-text\">";
      str += msg;
      str += "          <\/div>";
      str += "          <div class=\"cm-msg-button\">";
      str += "            <ul>";   
      str += btn_obj;
      str += "            <\/ul>";
      str += "          <\/div>";
      str += "        <\/div>";
      $(".chat-logs").append(str);
      $("#cm-msg-"+INDEX).hide().fadeIn(300);   
      $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);
      $("#chat-input").attr("disabled", true);
    }
    
    $(document).delegate(".chat-btn", "click", function() {
      var value = $(this).attr("chat-value");
      var name = $(this).html();
      $("#chat-input").attr("disabled", false);
      generate_message(name, 'self');
    })
    
    $("#chat-circle").click(function() {    
      $("#chat-circle").toggle('scale');
      $(".chat-box").toggle('scale');
    })
    
    $(".chat-box-toggle").click(function() {
      $("#chat-circle").toggle('scale');
      $(".chat-box").toggle('scale');
    })
    
  })
    }]);
