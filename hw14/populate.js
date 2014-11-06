// Retrieve
var MongoClient = require('mongodb').MongoClient;

// Connect to the db
MongoClient.connect("mongodb://jmorneau:julia1117@ds051640.mongolab.com:51640/comp398", function(err, db) {
  	if(err) { return console.dir(err); }
   	console.log("We are connected");

	var collection = db.collection('hw14');

	if (collection.find(function(err, result) {}) !== null) {
		collection.remove(function(err, result) {});
		console.dir("removed collection's documents");
	}

	db.createCollection('hw14', {strict:true}, function(err, collection) {});

  	var doc1 = {'hello':'doc1'};
  	var doc2 = {'hello':'doc2'};
  	var lotsOfDocs = [{'hello':'doc3'}, {'hello':'doc4'}];

  	for (i = 0; i < 2500; i++)
	{
		if(i%3==0){
			collection.insert(doc1, function(err, result) {});
		}
		if(i%3==1){
			collection.insert(doc2, function(err, result) {});
		}
		if(i%3==2){
			collection.insert(lotsOfDocs, function(err, result) {});
		}
	}
	console.dir('added to hw14');

});

