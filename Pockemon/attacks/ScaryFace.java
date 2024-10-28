package attacks;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;
import ru.ifmo.se.pokemon.Stat;

public class ScaryFace extends StatusMove {
    public ScaryFace() {
        super(Type.NORMAL, 0, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        if (p.getStat(Stat.SPEED) > -6) {
            p.setMod(Stat.SPEED, -1);
        }
        if (p.getStat(Stat.SPEED) > -6) {
            p.setMod(Stat.SPEED, -1);
        }
    }

    @Override
    protected String describe() {
        return "использует Scary Face";
    }
}
