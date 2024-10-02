import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Matrix {
    public static int[] createArray() {
        int[] z1 = new int[7]; 
        int index = 1;
        for (int i = 16; i >= 6; i -= 2) {
            z1[index] = i;
            index++;
        }
        return z1;
    }
    public static float[] createRandomArray() {
        float[] x1 = new float[16]; 
        Random random = new Random();

        for (int i = 1; i <= 15; i++) { 
            x1[i] = -14.0f + random.nextFloat() * (15.0f + 14.0f);
        }
        return x1;
    }
    public static float calculateElement(int zi, float x, double e, double pi) {
        if (zi == 14) {
            return  (float) (1 / Math.pow(e, Math.pow(2 * pi * (Math.pow(4 / Math.abs(x), 2)), Math.cos(Math.log(Math.abs(x))))));
        }
        else if(zi == 6 || zi == 8 || zi == 10) {
            return (float) Math.pow((Math.pow(e, Math.pow(x, x / 2)) / 2), 2);
        }
        else {
            return (float) Math.cos(Math.pow((Math.asin((x + 0.5) / 29) + 0.5), Math.pow(Math.pow(e, x), 2.75 / (x - 3))));
        }
    }
    public static void printMatrix(float[][] z) {
        for (int i = 1; i <= 6; i++) {
            for (int j = 1; j <= 15; j++) {
                System.out.printf("%.3f ", z[i][j]);
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        int[] z1 = createArray();
        float[] x1 = createRandomArray();

        double e = Math.E, pi = Math.PI;
        float[][] z = new float[7][16];
        for (int i = 1; i <= 6; i++) { 
            for (int j = 1; j <= 15; j++) { 
                float x = x1[j];
                z[i][j] = calculateElement(z1[i], x1[j], e, pi);
            }
        }
        printMatrix(z);

    }
}
