function solution(sizes) {
    
    sizes.map((size, idx)=> {
        if(size[0] > size[1]){
            let temp = size[0];
            sizes[idx][0] = size[1];
            sizes[idx][1] = temp;
        }
    })
    
    let w_max = 0, h_max = 0;
    sizes.map((size) => {
        w_max = size[0] > w_max ? size[0] : w_max;
        h_max = size[1] > h_max ? size[1] : h_max;
    })
    
    return w_max * h_max;
}