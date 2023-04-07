 let N = parseInt(readline());

 let factors = [];   
 let i = 2;
 while (i <= N) {
     if (N % i === 0) {
         factors.push(i);
         N /= i;
     } else {
         i++;
     }
 }
 
 console.log(factors.reduce((a, b) => a + b, 0));