x=Math.random();

"use strict";
const ps = require(`prompt-sync`);
const prompt = ps();

let a=Number(prompt("Enter a no.:"));
let b=Number(prompt("Enter a no.:"));
let op=prompt("Enter the operator.:");


if(x<0.1){
    if(op=="+"){
        console.log(a-b);
    }
    else if(op=="-"){
        console.log(a/b);
    }
    else if(op=="*"){
        console.log(a+b);
    }
    else if(op=="/"){
        console.log(a**b);
    }


}
else{
    if(op=="+"){
        console.log(a+b);
    }
    else if(op=="-"){
        console.log(a-b);
    }
    else if(op=="*"){
        console.log(a*b);
    }
    else if(op=="/"){
        console.log(a/b);
    }
}