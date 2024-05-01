function solution(answers) {
    var answer = [];
    
    const one = [1, 2, 3, 4, 5];
    const two = [2, 1, 2, 3, 2, 4, 2, 5];
    const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let cnt1=0, cnt2=0, cnt3=0;
    
    answers.forEach((ans, idx) => {
        if(one[idx%5] == ans) {cnt1 += 1;}
        if(two[idx%8] == ans) {cnt2 +=1;}
        if(three[idx%10] == ans) {cnt3 += 1;}
    })
    
    const max = Math.max(cnt1, cnt2, cnt3);
    
    if(cnt1 == max) answer.push(1);
    if(cnt2 == max) answer.push(2);
    if(cnt3 == max) answer.push(3);
    
    return answer;
}