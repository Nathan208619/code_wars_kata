fn move_zeros(arr: &[u8]) -> Vec<u8> {
    let mut zero_count: u8 = 0;
    let mut list: Vec<u8> = [].to_vec();

    for i in arr {
        if *i == 0
        {
            zero_count += 1
        }
        else
        {
            list.push(*i);
        }
    }

    while zero_count > 0
    {
        list.push(0);
        zero_count -= 1;
    }
    return list;
}

fn main() {
   let list = move_zeros(&[1, 2, 0, 1, 0, 1, 0, 3, 0, 1]);
    println!("{:?}", list);
}
