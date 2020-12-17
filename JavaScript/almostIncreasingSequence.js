function almostIncreasingSequence(seq) {
    var bad=0
    for(var i=1;i<seq.length;i++) 
    if(seq[i]<=seq[i-1]) {
      bad++
      if(bad>1) return false
      if(seq[i]<=seq[i-2]&&seq[i+1]<=seq[i-1]) return false
    }
    return true
  }
  

  function almostIncreasingSequence2(sequence) {
    let removed = 0;
    let i = 0;
    while(removed < 2 && i < sequence.length) {
       if(sequence[i] <= sequence[i-1]) {
          removed ++
          if(sequence[i] <= sequence[i-2] && sequence[i+1] <= sequence[i-1]) return false
         }
       i++;
    }
    return removed < 2;
 }