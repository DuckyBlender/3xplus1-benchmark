# Simple script to run all benchmarks in the benchmarks folder

import os
import sys
import datetime

# 0.0. Set current directory
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
print(f"Current directory: {path}")
# 0.1. Check if the compiled folder exists
if not os.path.exists("Compiled"):
    # Create the benchmarks folder
    os.mkdir("Compiled")
    print("Created compiled folder.")

# 1. Compile C and C++ benchmarks
print("Compiling C benchmark...")
now = datetime.datetime.now()
# os.system("cd Benchmarks/C && gcc - O3 -o benchmark_c benchmark_c.c")
os.system("gcc -O3 -o Compiled/benchmark_c Benchmarks/C/main.c")
print(
    f"C benchmark compiled in {str(datetime.datetime.now() - now)} seconds.")

print("Compiling C++ benchmark...")
os.chdir(path)
now = datetime.datetime.now()
# os.system("cd Benchmarks/C++ && g++ - O3 -o benchmark_cpp benchmark_cpp.cpp")
os.system("g++ -O3 -o Compiled/benchmark_cpp Benchmarks/C++/main.cpp")
print(
    f"C++ benchmark compiled in {str(datetime.datetime.now() - now)} seconds.")

# 2. Compile Rust benchmark
print("Compiling Rust benchmark...")
os.chdir(path)
now = datetime.datetime.now()
# os.system("cd Benchmarks/Rust && rustc -O -o benchmark_rust benchmark_rust.rs")
os.system("rustc -O -o Compiled/benchmark_rust Benchmarks/Rust/main.rs")
print(
    f"Rust benchmark compiled in {str(datetime.datetime.now() - now)} seconds.")

# 3. Compile Java benchmark
print("Compiling Java benchmark...")
os.chdir(path)
now = datetime.datetime.now()
# os.system("cd Benchmarks/Java && javac Main.java")
os.system("javac Benchmarks/Java/Main.java -d Compiled")
print(
    f"Java benchmark compiled in {str(datetime.datetime.now() - now)} seconds.")

# 4. Run benchmarks
print("Running benchmarks...")
os.chdir(path)
now = datetime.datetime.now()
print("Running Python benchmark...")
os.system("python3 benchmark.py")
print("Running C benchmark...")
os.system("Compiled/benchmark_c")
print("Running C++ benchmark...")
os.system("Compiled/benchmark_cpp")
print("Running Rust benchmark...")
os.system("Compiled/benchmark_rust")
print("Running Java benchmark...")
os.system("java -cp Compiled Main")

print(f"Benchmarks ran in {str(datetime.datetime.now() - now)} seconds.")
