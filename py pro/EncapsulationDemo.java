class Encapsulate {
    private String geekName;
    private int geekRoll;
    private int geekAge;

    public void setAge(int newAge) {
        geekAge = newAge;
    }

    public void setName(String newName) {
        geekName = newName;
    }

    public void setRoll(int newRoll) {
        geekRoll = newRoll;
    }

    public String getName() {
        return geekName;
    }

    public int getRoll() {
        return geekRoll;
    }

    public int getAge() {
        return geekAge;
    }
}

public class EncapsulationDemo {
    public static void main(String args[]) {
        Encapsulate obj = new Encapsulate();
        obj.setName("Harish");
        obj.setAge(19);
        obj.setRoll(05);

        System.out.println("Geek's name:" + obj.getName());
        System.out.println("Geek's age:" + obj.getAge());
        System.out.println("Geek's roll:" + obj.getRoll());
    }
}
