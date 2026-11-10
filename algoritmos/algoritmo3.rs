//Algoritmo 3: Manejo de literales numericos, cadenas, caracteres y tipos de datos
//Cesar Moreira

fn main() {
    // Enteros decimales
    let entero = 150;
    let separado = 98_222;
    let con_signo = -25i32;
    let sin_signo = 57u32;

    //Enteros en otras bases
    let hexadecimal = 0xFFu32;
    let octal = 0o755;
    let binario = 0b1010u8;

    //Numeros flotantes
    let decimal = 3.1416;
    let flotante_f32 = 2.5f32;
    let flotante_f64 = 10.0f64;
    let cientifico = 1e5;
    let exponente_negativo = 2.5e-3;

    //Cadenas
    let saludo = "Hola, mundo";
    let mensaje = "Estoy aprendiendo Rust";
    let texto_escapado = "Primera linea\nSegunda linea";

    //Caracteres
    let inicial = 'C';
    let digito = '7';
    let salto = '\n';

    //Tipos de datos
    let edad: i32 = 25;
    let cantidad: u64 = 100u64;
    let temperatura: f64 = 36.5;
    let activo: bool = true;
    let letra: char = 'R';
    let texto: &str = "Texto prestado";
    let nombre: String = String::from("Cesar");

    //Prueba de literales numericos
    let maximo_u128: u128 = 340282366920938463463374607431768211455u128;
    let binario_separado: u8 = 0b1111_0000u8;
    let cientifico_f64: f64 = 6.022e23f64;

    // Prueba de cadenas, caracteres y tipos
    let comillas_escapadas = "Rust dice: \"Hola\"";
    let tabulacion: char = '\t';
    let desactivado: bool = false;
    let tamano: usize = 1_024usize;

    let comilla_simple: char = '\'';
    let barra_invertida: char = '\\';
}
