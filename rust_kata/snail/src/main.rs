fn main() {
    let square = &[
            vec![1,2,3],
            vec![4,5,6],
            vec![7,8,9],
        ];

    let mut snail: Vec<i32> = [].to_vec();

    let mut n = square.len();
    let mut h = 0;
    let mut w = 0;

    while n > 0 {
        while w < n {
            snail.push(square[h][w]);
            w += 1;
        }
        snail.pop();
        w -= 1;
        while h < n {
            snail.push(square[h][w]);
            h += 1;
        }
        snail.pop();
        h -= 1;
        while w > 0 {
            snail.push(square[h][w]);
            w -= 1;
        }
        while h > 0 {
            snail.push(square[h][w]);
            h -= 1;
        }
        h += 1;
        w += 1;
        n -= 1;
        println!("{:?}", n);
    }
    // println!("{:?}", n);
    // println!("{:?}", w);
    // println!("{:?}", h);
    

    println!("{:?}", snail);

}
