// First time writing in rust

//use std::{thread, time};

fn main() {
    println!("Start!");
    let mut num: u64;

    for i in 1..1000001 {
//        println!("Current number: {}", i);
        num = i;
        while num != 1 {
            if num % 2 == 0 {
                num = num / 2;
//                println!("Divided by 2! {}", num);
            } else if num % 2 == 1 {
                num = 3 * num + 1;
//                println!("Did 3x+1! {}", num);
            }
        }
//        thread::sleep(time::Duration::from_secs(1));
    }
    println!("End!");
}

// TODO: Count time