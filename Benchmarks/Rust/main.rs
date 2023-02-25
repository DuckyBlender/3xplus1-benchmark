fn main() {
    println!("Start!");
    use std::time::Instant;
    let now = Instant::now();
    let mut num: u64;

    for i in 1..1000001 {
        num = i;
        while num != 1 {
            if num % 2 == 0 {
                num = num / 2;
            } else if num % 2 == 1 {
                num = 3 * num + 1;
            }
        }
    }
    let elapsed = now.elapsed();
    println!("End! This took {:.5?} seconds!", elapsed);
}
