function solution(brown, yellow) {
    var answer = [];
    
    let sum = brown + yellow;
    let w = brown / 2, h = 2;
    
    while(w >= h) {
        
        if(w * h == sum) {
            answer.push(w);
            answer.push(h);
            break;
        }
        w -= 1;
        h += 1;
    }
    
    return answer;
}