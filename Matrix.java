import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Matrix {
    public static void main(String[] args) {
        int[] z1 = new int[7]; 
        int index = 1;
        for (int i = 16; i >= 6; i -= 2) {
            z1[index] = i;
            index++;
        }

        for (int i = 1; i < z1.length; i++) { 
            System.out.print(z1[i] + " ");
        }
        System.out.println();

        float[] x1 = new float[16]; 
        
        Random random = new Random();
        
        for (int i = 1; i <= 15; i++) { 
            x1[i] = -14.0f + random.nextFloat() * (15.0f + 14.0f);
        }

        for (int i = 1; i <= 15; i++) { 
            System.out.printf("%.3f ", x1[i]); 
        }
        System.out.println();

        float e = 2.7182f, pi = 3.14f;
        float[][] z = new float[7][16];
        
        List<Integer> v = Arrays.asList(6, 8, 10); 
        for (int i = 1; i <= 6; i++) { 
            for (int j = 1; j <= 15; j++) { 
                double x = x1[j];
                
                if (z1[i] == 14) {
                    z[i][j] = (float) (1 / Math.pow(e, Math.pow(2 * pi * (Math.pow(4 / Math.abs(x), 2)), Math.cos(Math.log(Math.abs(x))))));
                } 
                else if (v.contains(z1[i])) {
                    z[i][j] = (float) Math.pow((Math.pow(e, Math.pow(x, x / 2)) / 2), 2);
                } 
                else {
                    z[i][j] = (float) Math.cos(Math.pow((Math.asin((x + 0.5) / 29) + 0.5), Math.pow(Math.pow(e, x), 2.75 / (x - 3))));
                }
                 System.out.printf("%.3f ", x1[i]); 
            }
            System.out.println();
        }
    }
}
