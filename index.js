const express = require("express")
global.app = express()
global.confi= require("./confi.js").confi

app.use(bodyparser.urlencoded({extended:true}))

var db =[]
var registroactividad = []