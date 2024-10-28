package attacks;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;
import ru.ifmo.se.pokemon.Stat;

public class Swagger extends StatusMove {
    public Swagger() {
        super(Type.NORMAL, 0, 85);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        if (p.getStat(Stat.ATTACK) < 6) {
            p.setMod(Stat.ATTACK, 1);
        }
        if (p.getStat(Stat.ATTACK) < 6) {
            p.setMod(Stat.ATTACK, 1);
        }
        Effect.confuse(p);
    }

    @Override
    protected String describe() {
        return "использует Swagger";
    }
}
