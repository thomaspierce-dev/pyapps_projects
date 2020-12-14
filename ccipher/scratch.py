{ “apiVersion”: “v1”,
“kind”: “Pod”,
“metadata”:
    { “name”: “rss-site”,
    “labels”:
        { “app”: “web” } },
“spec”:
    { “containers”:
        [{ “name”: “front-end”, “image”: “nginx”,
           “ports”:
                [{ “containerPort”: “80” }] },

        [{ “name”: “rss-reader”,
           “image”: “nickchase/rss-php-nginx:v1”,
           “ports”:
                [{ “containerPort”: “88” }] }] } }