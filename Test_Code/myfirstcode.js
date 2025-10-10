console.log("BS ECE 1-2 demo");
function countdown(num){
    console.log(num);
    if (num > 0) {
      setTimeout(() => countdown(num - 1), 1000);
    }
}
countdown(10);