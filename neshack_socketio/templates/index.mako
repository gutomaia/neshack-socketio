<html>
    <head>
        <title>NES Hack</title>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">

        <link rel="stylesheet" href="/static/css/component/bootstrap/css/bootstrap.css">

        <link rel="stylesheet" href="/static/css/component/startbootstrap-sb-admin-2/css/sb-admin-2.css">

        <link rel="stylesheet" href="/static/css/component/font-awesome/css/font-awesome.css" type="text/css">

        <script>
        var require = {
            shim : {
                "bootstrap" : { "deps" : ['jquery'] },
                "backbone":  { "deps" : ['underscore'] },
                "phaser": { "exports": "Phaser" },
                "socket.io": { "exports": "io" }
            },
            paths: {
                "app": "/static/js/app",
                "jquery" : "/static/js/component/jquery/jquery",
                "bootstrap" :  "/static/js/component/bootstrap/bootstrap",
                "backbone": "/static/js/component/backbone/backbone",
                "backbone.babysitter" :  "/static/js/component/backbone.babysitter/backbone.babysitter",
                "backbone.wreqr" :  "/static/js/component/backbone.wreqr/backbone.wreqr",
                "backbone.marionette" :  "/static/js/component/backbone.marionette/backbone.marionette",
                "phaser" :  "/static/js/component/phaser/phaser",
                "socket.io": "/static/js/component/socket.io-client/socket.io",
                "underscore": "/static/js/component/underscore/underscore",
                "text": "/static/js/component/requirejs-text/text"
            }
        };
        </script>
    </head>
    <body>
        <div id="wrapper">oi</div>
        <script type="text/javascript" data-main="/static/js/init.js" src="/static/js/component/requirejs/require.js"></script>
    </body>
</html>
