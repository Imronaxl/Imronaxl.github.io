public class Zma {
    public static void main(String[] args) {
        long[] z = new long[6];

        int index = 0;
        for (long i = 16; i >= 6; i -= 2) {
            z[index] = i;
            index++;
        }

        for (long num : z) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
