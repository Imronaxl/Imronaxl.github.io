import java.util.Random;

public class Rand {
    public static void main(String[] args) {
        float[] x = new float[15];
        
        Random random = new Random();
        
        for (int i = 0; i < x.length; i++) {
            x[i] = -14.0f + random.nextFloat() * (15.0f + 14.0f);
        }

        for (float num : x) {
        System.out.printf("%.3f ", num); 
        }
        System.out.println();
    }
}

