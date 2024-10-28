package attacks;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.PhysicalMove;
public class DreamEater extends SpecialMove {
    public DreamEater() {
        super(Type.PSYCHIC, 100, 100);
    }

    @Override
    protected void applyOppDamage(Pokemon def, double damage) {
        // if (def.getCondition() == Status.SLEEP) {
            super.applyOppDamage(def, damage);

            def.setMod(Stat.HP, (int) Math.round(damage / 2));
        // } 
    }

    @Override
    protected String describe() {
        return "использует Dream Eater!";
    }
}
