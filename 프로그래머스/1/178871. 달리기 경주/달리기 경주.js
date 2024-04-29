function solution(players, callings) {
    
    const myMap = new Map();
    
    players.forEach((item, idx) => {
        myMap.set(item, idx);
    })

    callings.forEach((item) => {
        let idx = myMap.get(item);

        let temp = players[idx -1];
        players[idx-1] = players[idx];
        players[idx] = temp;
        
        myMap.set(item, idx-1);
        myMap.set(temp, idx);
    })
    
    return players;
}