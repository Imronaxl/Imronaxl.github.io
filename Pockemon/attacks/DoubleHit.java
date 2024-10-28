package attacks;

import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;
import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Stat;

public class DoubleHit extends PhysicalMove {

    public DoubleHit() {
        super(Type.NORMAL, 35, 90); 
    }

    @Override
    protected void applyOppDamage(Pokemon def, double damage) {
        for (int i = 0; i < 2; i++) {
            if (def.isAlive()) {  
                def.setMod(Stat.HP, (int) Math.round(damage));
            }
        }
    }

    @Override
    protected String describe() {
        return "использует Double Hit";
    }
}
