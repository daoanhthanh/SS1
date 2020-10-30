package OOP;

public class car extends vehicle {
    int no_wheel;
    
    public car(String ten, String engine, int so_banh) {
        super(ten, engine);
        this.no_wheel = so_banh;
        // TODO Auto-generated constructor stub
    }
    public static void main(String[] args) {
        car merc = new car("Mescerdes", "V4 turbo", 4);
        System.out.println(merc.name);
    }
}
