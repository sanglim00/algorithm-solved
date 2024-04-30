function solution(name, yearning, photo) {
    var answer = [];
    const myMap = new Map();
    
    name.forEach((user, idx)=> {
        myMap.set(user, yearning[idx]);
    })
    
    photo.forEach((item) => {
        let score = 0;
        item.map((user) => {
            score += myMap.get(user) ? myMap.get(user) : 0;
        })
        answer.push(score);
    })
    
    return answer;
}