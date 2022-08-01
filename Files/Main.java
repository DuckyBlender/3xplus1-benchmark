public class Main {
    public static void main(String[] args) throws InterruptedException {
        int x;
        System.out.println("Start!");

        long startTime = System.currentTimeMillis();
        for (int i = 1; i <= 1000000; i++)
        {
            x = i;
            while (true) {
                if (x <= 1) {
                    break;
                } else if (x % 2 == 1) {
                    x = 3 * x + 1;
                } else if (x % 2 == 0) {
                    x /= 2;
                }
            }
        }

        long stopTime = System.currentTimeMillis();
        long elapsedTime = stopTime - startTime;
        System.out.println("End! This took " + (double)elapsedTime/1000 + " seconds");
    }
}
