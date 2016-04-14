angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
    
  

      .state('menu.home', {
    url: '/',
    views: {
      'side-menu21': {
        templateUrl: 'templates/home.html',
        controller: 'homeCtrl'
      }
    }
  })

  .state('menu.yourIngredients', {
    url: '/ingredients',
    views: {
      'side-menu21': {
        templateUrl: 'templates/yourIngredients.html',
        controller: 'yourIngredientsCtrl'
      }
    }
  })

  .state('menu', {
    url: '/menu',
    templateUrl: 'templates/menu.html',
    abstract:true
  })

  .state('login', {
    url: '/page7',
    templateUrl: 'templates/login.html',
    controller: 'loginCtrl'
  })

  .state('signup', {
    url: '/signup',
    templateUrl: 'templates/signup.html',
    controller: 'signupCtrl'
  })

  .state('menu.addIngredients', {
    url: '/add',
    views: {
      'side-menu21': {
        templateUrl: 'templates/addIngredients.html',
        controller: 'addIngredientsCtrl'
      }
    }
  })

  .state('menu.userIgredients', {
    url: '/useringredients',
    views: {
      'side-menu21': {
        templateUrl: 'templates/userIgredients.html',
        controller: 'userIgredientsCtrl'
      }
    }
  })

  .state('menu.user', {
    url: '/user',
    views: {
      'side-menu21': {
        templateUrl: 'templates/user.html',
        controller: 'userCtrl'
      }
    }
  })

  .state('menu.profile', {
    url: '/profile',
    views: {
      'side-menu21': {
        templateUrl: 'templates/profile.html',
        controller: 'profileCtrl'
      }
    }
  })

  .state('menu.match', {
    url: '/match',
    views: {
      'side-menu21': {
        templateUrl: 'templates/match.html',
        controller: 'matchCtrl'
      }
    }
  })

  .state('menu.friends', {
    url: '/friends',
    views: {
      'side-menu21': {
        templateUrl: 'templates/friends.html',
        controller: 'friendsCtrl'
      }
    }
  })

  .state('menu.range', {
    url: '/range',
    views: {
      'side-menu21': {
        templateUrl: 'templates/range.html',
        controller: 'rangeCtrl'
      }
    }
  })

$urlRouterProvider.otherwise('/page7')

  

});