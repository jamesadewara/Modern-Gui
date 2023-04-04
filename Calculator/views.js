//fixme: writing and reading of json uses node.js so hasn't been properly finished.
const calculator = {
  expression : '', // this will be the frontend that the user will see
  express : '', // what really happens
};

const obj = [
  {
      "date" : "35 min ago",
      "expression" : "2 x 5",
      "express" : "10",
  }
]

var add_updates = [];

//get the elements that will display the calculator items
var calculator_screen = document.getElementById("calculator-screen");
calculator_screen.value = calculator.expression;
var calculator_input = document.getElementById("calculator-input");

function saveJson(){
  var fs = require('fs');
  var dictstring = JSON.stringify(obj);
  fs.writeFile("history.json", dictstring);
}

function updateHistory(){
  obj = [
    {
      "datetime" : Date.datetime,
      "expression" : calculator.expression,
      "express" : calculator.express,
    }
  ]
  add_updates.push(obj);
  JSON.stringify(add_updates);
}

function updateExpress(item){
  calculator.express = calculator.express + item;

  try {//if an error occuress during evluation do nothing
    calculator_input.innerText = eval(calculator.express);
  } catch (error) {
  }
  
}

function updateExpression(item){
  //add the expression to the calc screen
  calculator.expression = calculator.expression + item;
  calculator_screen.value = (calculator.expression);
}



function updateCalculations(value, symbol){
  updateExpression(symbol);//the front end
  updateExpress(value);// the backend 
}

function equalsTo(){
  calculator.express = eval(calculator.express)
  calculator.expression = calculator.express; //add the evaluated express value to the expression
  calculator_screen.value = calculator.expression;
  calculator.express = '0'; //set expression and express to empty
  calculator.expression = '';
  calculator_input.innerText = calculator.express;
}

function answer(){
  //add the values to the json
  obj.push(
    {
      "date" :  new Date().getTime(),
      "expression" : calculator.expression ,
      "express" : calculator.express,
  }
  )
  // /saveJson()
  calculator.express = eval(calculator.express)
  calculator_screen.value = calculator.express;
  calculator.expression = calculator.express;
  calculator_input.innerText = '0';
  

}

function clearValues(){
  calculator.express = '';
  calculator.expression = '';
  calculator_input.innerText = calculator.express;
  calculator_screen.value = calculator.expression;
}

function deleteValue(){
  calculator.express = calculator.express.slice(0, (calculator.express.length)-1); //remove the last character from the string
  calculator.expression = calculator.expression.slice(0, (calculator.expression.length)-1);
  calculator_input.innerText = calculator.express;
  calculator_screen.value = calculator.expression;
}

function percentage(value, symbol){
  updateExpression(symbol);//the front end
  updateExpress(value);// the backend 
  if (calculator.expression[0] == '%'){ //check if the first expression is %
    calculator.express = '' 
    calculator_input.innerText = calculator.express;
  }
  answer();
  calculator.express = calculator.expression; 
  calculator_input.innerText = calculator.express;
  
  
}
