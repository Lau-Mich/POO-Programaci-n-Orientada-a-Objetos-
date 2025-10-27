//agenda de contactos
//aqui es casi los mismo q en python esta clase representa un contacto general con tres datos básicos:
//nombre, teléfono y correo electrónico.

// 12.implementa en java las clases de tu diagrama.
class Contacto {
    protected String nombre;
    protected String telefono;
    protected String email;

    public Contacto(String nombre, String telefono, String email) {
        this.nombre = nombre;
        this.telefono = telefono;
        this.email = email;
    }

    // 14. muestra un ejemplo de polimorfismo en tu código.
    //polimorfismo:
    //aqui muestra la información general del contacto.
    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Teléfono: " + telefono);
        System.out.println("Email: " + email);
    }
}


// 13. agrega atributos, métodos y una relación de herencia.
// Esta clase hereda de Contacto y agrega un nuevo dato osea el cumpleaños.
class ContactoAmigo extends Contacto {
    private String cumpleaños;  //aqui ps el atrivuto de los amiguitos

    //aqui llama al constructor de la clase padre con "super"
    // para inicializar nombre, teléfono y email,
    // y además inicializa el cumpleaños.
    public ContactoAmigo(String nombre, String telefono, String email, String cumpleaños) {
        super(nombre, telefono, email); 
        this.cumpleaños = cumpleaños;
    }
    //aqui se aplica el polimorfismo osea
    //se muestra primero la info basica (de Contacto)
    // y luego se agrega el dato específico del amigo (cumpleaños).
    @Override
    public void mostrarInfo() {
        super.mostrarInfo();  // Muestra los datos generales
        System.out.println("Cumpleaños: " + cumpleaños);
    }
}
//esta clase hereda de Contacto y agrega un nuevo dato: la empresa.
//representa un contacto laboral o profesional.
class ContactoTrabajo extends Contacto {
    private String empresa;  //este es el atributo propio de los contactos de trabajo

    //igual q antes use "super" para inicializar los datos básicos
    // y luego se asigna la empresa.
    public ContactoTrabajo(String nombre, String telefono, String email, String empresa) {
        super(nombre, telefono, email); 
        this.empresa = empresa;
    }
    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Empresa: " + empresa);
    }
}


//esta clase contiene el método main(), osea punto de entrada del programa
public class Agenda_de_contactos {
    public static void main(String[] args) {

        //polimorfismo:
        //aqui es como hacer lo de tener los contactos pre definidos
        //los tengo clasificados en el contacto normal, el amigo, y el de trabajo 

        Contacto contacto1 = new Contacto("Valery Rincon", "310-123-4567", "valery@email.com");
        Contacto contacto2 = new ContactoAmigo("Luis Riveros", "320-987-6543", "luis@email.com", "15/07");
        Contacto contacto3 = new ContactoTrabajo("Paulo Gutierrez", "315-555-7890", "paulo@trabajo.com", "Diamante.SAS");
//utilice el "new" porq sirve para crear un objeto a partir de una clase, asi ya podia hacer los contactod



        // 15. ejecuta tu programa y muestra la salida.
        //aqui ya va la impresion de toda la agenda
        //(al inicio me quedo todo desordenado AJAJA no sabia q podia hacer en java esto tambien)

        System.out.println("=== Agenda de Contactos ===");
        contacto1.mostrarInfo();
        System.out.println("-------------------------");
        contacto2.mostrarInfo();
        System.out.println("-------------------------");
        contacto3.mostrarInfo(); 
        System.out.println("-------------------------");
        }    }