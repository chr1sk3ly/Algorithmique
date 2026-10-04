interface RegexInterface {
    public boolean reconnaitre_epsilon();

    public RegexInterface derive(Character a);
}

class Union implements RegexInterface {
    private RegexInterface expr1, expr2;

    public Union(RegexInterface exp1, RegexInterface exp2) {
        this.expr1 = exp1;
        this.expr2 = exp2;
    }

    @Override
    public boolean reconnaitre_epsilon() {
        return expr1.reconnaitre_epsilon() || expr2.reconnaitre_epsilon();
    }

    @Override
    public RegexInterface derive(Character a) {
        return new Union(expr1.derive(a), expr2.derive(a));
    }
}

class Concat implements RegexInterface {
    private RegexInterface expr1, expr2;

    public Concat(RegexInterface exp1, RegexInterface exp2) {
        this.expr1 = exp1;
        this.expr2 = exp2;
    }

    @Override
    public boolean reconnaitre_epsilon() {
        return expr1.reconnaitre_epsilon() && expr2.reconnaitre_epsilon();
    }

    @Override
    public RegexInterface derive(Character a) {
        if (expr1.reconnaitre_epsilon())
            return new Union(new Concat(expr1.derive(a), expr2), expr2.derive(a));

        return new Concat(expr1.derive(a), expr2);
    }
}

class Etoile implements RegexInterface {
    private RegexInterface expr1;

    public Etoile(RegexInterface exp1) {
        this.expr1 = exp1;
    }

    @Override
    public boolean reconnaitre_epsilon() {
        return true;
    }

    @Override
    public RegexInterface derive(Character a) {
        return new Concat(expr1.derive(a), expr1);
    }
}

class LangageVide implements RegexInterface {
    public LangageVide() {}
    
    @Override
    public boolean reconnaitre_epsilon() {
        return false;
    }

    @Override
    public RegexInterface derive(Character a) {
        return new LangageVide();
    }
}

class Epsilon implements RegexInterface {
    public Epsilon() {
    }

    @Override
    public boolean reconnaitre_epsilon() {
        return true;
    }

    @Override
    public RegexInterface derive(Character a) {
        return new LangageVide();
    }
}

class SymboleNonTerminal implements RegexInterface {
    private Character expr;

    public SymboleNonTerminal(Character exp) {
        this.expr = exp;
    }

    @Override
    public boolean reconnaitre_epsilon() {
        return false;
    }

    @Override
    public RegexInterface derive(Character a) {
        if (a == expr)
            return new Epsilon();
        return new LangageVide();
    }
}

class Regex {
    public static void main(String argv[]) {
        RegexInterface a = new Union(new SymboleNonTerminal('a'), new Etoile(new Concat(new SymboleNonTerminal('a'),new SymboleNonTerminal('b')))) ;

        System.out.println(a.reconnaitre_epsilon());
    }
}