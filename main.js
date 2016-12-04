//stolen from here
//https://www.sitepoint.com/creating-and-handling-forms-in-node-js/

var http = require('http');
var fs = require('fs');
var formidable = require("formidable");
var util = require('util');

var server = http.createServer(function (req, res) {
    if (req.method.toLowerCase() == 'get') {
        displayForm(res);
    } else if (req.method.toLowerCase() == 'post') {
        processAllFieldsOfTheForm(req, res);
    }

});

function displayForm(res) {
    fs.readFile('form.html', function (err, data) {
        res.writeHead(200, {
            'Content-Type': 'text/html',
                'Content-Length': data.length
        });
        res.write(data);
        res.end();
    });
}

function processAllFieldsOfTheForm(req, res) {
    var form = new formidable.IncomingForm();

    form.parse(req, function (err, fields, files) {
        //Store the data from the fields in your data store.
        //The data store could be a file or database or any other store based
        //on your application.
        res.writeHead(200, {
            'content-type': 'text/plain'
        });
        res.write('received the data:\n\n');
        res.end(util.inspect({
            fields: fields,
            files: files
        }));
        
        a = fields.id
        b = fields.time
        
        console.log(!isNaN(parseInt(fields.id)))
        
        if(!isNaN(parseInt(fields.id)) && !isNaN(parseInt(fields.time)) && parseInt(fields.time) >= 60)
        {
            fs.appendFile('sendTo', a + "|" + b + "|0|0"+'\n', function (err) {
                console.log("appended: " + a + "|" + b + "|0|0")
            });
        }


        
    });
}

server.listen(1185);
console.log("server listening on 1185");
