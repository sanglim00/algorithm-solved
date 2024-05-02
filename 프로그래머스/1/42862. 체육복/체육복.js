function solution(n, lost, reserve) {

    let temp = reserve.map((i) => i);
    
    reserve = reserve.filter((i) => !lost.includes(i));
    lost = lost.filter((i) => !temp.includes(i));
    
    reserve.sort();
    lost.sort();
    
    let answer = n - lost.length;
  
    for (let i = 0; i < reserve.length; i++) {
        for (let j = 0; j < lost.length; j++) {
            if (reserve[i]-1 == lost[j] || reserve[i]+1 == lost[j]){
                reserve[i] = -1;
                lost[j] = -1;
                answer += 1;
                break;
            }
        }
    }
 
    return answer;
}