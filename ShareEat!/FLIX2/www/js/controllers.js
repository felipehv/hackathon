angular.module('app.controllers', [])

.controller('homeCtrl', function($scope) {

})

.controller('yourIngredientsCtrl', function($scope, $ionicPopup, $http) {

  $scope.showConfirm = function(a) {
    var confirmPopup = $ionicPopup.confirm({
      title: a,
      template: 'Are you sure you want to eat this ice cream?'
      });
    confirmPopup.then(function(res) {
      if(res) {
        console.log('You are sure');
      } else {
        console.log('You are not sure');
      }
    });
  };
  $scope.$on('$ionicView.enter', function(e) {
    debugger;
    var req = {
      method: 'GET',
      url: 'http://192.168.0.68:6970/get_user_ingredients/tamy',
      headers: {'Content-Type': undefined},
      data: {test: 'test'}
    }
    $http.get(req).
        then(
        function(response){
          $scope.matches =  response.data;
          $scope.showConfirm("Good")
        },
        function(response){
          $scope.matches = response;
          $scope.showConfirm(response.status);
        })
      });
})

.controller('loginCtrl', function($scope, $http) {
  $scope.showConfirm = function(a) {
    var confirmPopup = $ionicPopup.confirm({
      title: a,
      template: 'Are you sure you want to eat this ice cream?'
    });

    confirmPopup.then(function(res) {
      if(res) {
        console.log('You are sure');
      } else {
        console.log('You are not sure');
      }
    });
  };
    $scope.login = function(){
    req = $http.jsonp("http://192.168.0.68:6970/get_user_ingredients/tamy").
        then(
        function(data){
          $scope.eventos =  data;
        },
        function(data){
          $scope.eventos = data;
          $scope.showConfirm(data);
        })
    };
})

.controller('signupCtrl', function($scope) {
  $scope.login = function(){
  req = $http.get("http://localhost/eventos").
      then(
      function(data){
        $scope.eventos =  data;

      },
      function(data){
        $scope.eventos = data;
        $scope.showConfirm(data);
      })
  };
})

.controller('addIngredientsCtrl', function($scope) {
  var timeOut = 0;
  function onClick(but)
{
    //code
    clearTimeout(timeOut);
    timeOut = setTimeout(function (){onClick(but)},1000);
}

})

.controller('userCtrl', function($scope) {

})

.controller('profileCtrl', function($scope) {



})

.controller('matchCtrl', function($scope) {

})

.controller('friendsCtrl', function($scope) {

})



//
   
.controller('rangeCtrl', function($scope) {

//$scope.funcion = function(data){
        //$scope.value =  data;
      //},
  };

.controller('userIgredientsCtrl', function($scope) {

})
 