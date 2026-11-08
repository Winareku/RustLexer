//Algoritmo 2: Manejo de identificadores, palabras reservadas y operadores
//Israel Romero
//Nota: no usa literales numericos ni cadenas (parte de Cesar), solo true/false.

fn main() {
    //Identificadores
    let contador = true;
    let _temp = true;
    let total_ventas = true;
    let MAX_INTENTOS = true;
    let PI = true;
    let a1 = true;
    let _ = true;
 
    //Identificadores brutos
    let r#match = true;
    let r#try = true;
    let r#fn = true;
 
    //Etiquetas de bucle
    'externo: loop {
        'interno: loop {
            break 'externo;
        }
        continue 'externo;
    }
 
    //Macros
    println!(contador);
    print!(total_ventas);
    let mut v = vec![a1, _temp];
 
    //Macro frente a "distinto de" (no debe confundirse)
    let c1 = a != b;
    let c2 = a!=b;
    let c3 = a != !b;
 
    //Palabras reservadas: declaracion
    let mut x = true;
    const K: bool = true;
    static G: bool = true;
    struct Punto { x: bool }
    enum Color { Rojo }
    union Dato { a: bool }
    trait Rasgo { }
    impl Rasgo for Punto { }
    type Alias = bool;
 
    //Palabras reservadas: control de flujo
    if a { } else { }
    match a { b => c }
    loop { break; }
    while a { continue; }
    for i in a { }
    return a;
 
    //Palabras reservadas: literales booleanos
    let t = true;
    let f = false;
 
    //Palabras reservadas: modulos y visibilidad
    mod modulo { pub fn f() { } }
    use crate::modulo;
    use super::modulo;
    use self::modulo;
    fn nuevo() -> Self { }
 
    //Palabras reservadas: conversion y referencias
    let y = x as bool;
    let ref z = x;
    let cierre = move |a| a;
    let d: &dyn Rasgo = &p;
    fn gen<T>() where T: Rasgo { }
 
    //Palabras reservadas: asincronia y bajo nivel
    async fn tarea() { }
    let r = tarea().await;
    unsafe { }
    extern fn externa() { }
 
    //Identificadores que contienen palabras reservadas (deben ser ID)
    let letra = true;
    let format = true;
    let iffy = true;
    let Let = true;
    let selfie = true;
    let in_out = true;
    let _mut = true;
 
    //Operadores aritmeticos
    let suma = a + b;
    let resta = a - b;
    let prod = a * b;
    let cociente = a / b;
    let resto = a % b;
    let neg = -a;
 
    //Operadores de comparacion
    let r1 = a == b;
    let r2 = a != b;
    let r3 = a < b;
    let r4 = a > b;
    let r5 = a <= b;
    let r6 = a >= b;
 
    //Operadores logicos
    let l1 = a && b;
    let l2 = a || b;
    let l3 = !a;
    let l4 = !a && b || c;
 
    //Operadores de asignacion
    a = b;
    a += b;
    a -= b;
    a *= b;
    a /= b;
    a %= b;
 
    //Rangos
    for i in a..b { }
    for i in a..=b { }
 
    //Referencias, acceso y rutas
    let ref1 = &a;
    let ref2 = &mut a;
    let deref = *ref1;
    let campo = punto.x;
    let ruta = std::io::stdin();
    let mapa = HashMap::new();
    mapa.read_line(&mut entrada);
 
    //Flechas
    fn doble(x: bool) -> bool { x }
    match a { b => c, _ => d }
 
    //Clausuras (usan | y ||)
    let cl1 = |a, b| a + b;
    let cl2 = || a;
    let cl3 = |a| a || b;
 
    //Operadores pegados sin espacios
    let p1 = a+b-c*d/e%f;
    let p2 = a<=b&&c>=d||e!=f;
    let p3 = a..=b;
    let p4 = a..b;
    x+=y;
    x-=y;
}
 