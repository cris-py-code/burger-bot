<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido(data-aos="flip-up")
      .titulo-principal__numero
        span 5
      h1 Actividades didácticas

    .row.justify-content-center.align-items-center
      .col-lg-6
        figure
          img(src="@/assets/curso/temas/actividad/actividad_didactica.svg", alt="alt")
      .col-lg-6
        .crd.clr-paleYellow.p-4
          p.mb-0 Por cada componente formativo se puede proponer un máximo de dos actividades (mínimo debe ser 1) que los aprendices puedan realizar una vez han revisado los contenidos presentados y que refuercen la asimilación de los mismos.

        p.my-4 Entre las actividades propuestas se deben abordar todos los temas principales.

        p Son actividades que no generan evaluación y que funcionarán independiente del LMS.

    separador

    #t_5_1
    
    .titulo-segundo.color-acento-contenido
      h2 5.1 Cuestionarios

    .tarjeta.clr--gris.p-5.mb-4
      .row.justify-content-around.align-items-center
        .col-8.col-lg-5.mb-4.mb-md-0
          img(src="@/assets/curso/temas/actividad/actividad_02.png").mb-3

        .col-md.col-lg-6
          h3 Ejemplo cuestionario
          p.mb-4 #[strong Instrucciones.] Lea la afirmación de cada ítem y luego señale la respuesta correcta según corresponda.

          a.boton.boton--b(:href="obtenerLink('/actividades/AD2/index.html')" target="_blank")
            span Realizar
            i.fas.fa-puzzle-piece

    .row
      .col-lg-12.order-2.order-lg-1
        TabsA.color-acento-botones
          .tarjeta.clr--gris.p-4(titulo="Requerimientos")
            ul.lista-ul.mb-0
              li
                i.fas.fa-angle-right.txt--green
                | Las indicaciones, el mensaje de correcto e incorrecto debe estar la redacción en segunda persona.
              li
                i.fas.fa-angle-right.txt--green
                | El aprendiz recibe una retroalimentación cuando responde de manera correcta o incorrecta cada pregunta.
              li
                i.fas.fa-angle-right.txt--green
                | Al final de la actividad se muestra una retroalimentación de felicitación si logra el 70% de respuestas correctas o retroalimentación de mejora si es inferior a este porcentaje.
              li
                i.fas.fa-angle-right.txt--green
                | Las preguntas pueden ser de los siguientes tipos: Opción múltiple única respuesta, Falso o verdadero y opción múltiple con múltiple respuesta.
              li
                i.fas.fa-angle-right.txt--green
                | Por pregunta deben existir máximo 4 opciones de respuesta.
              li
                i.fas.fa-angle-right.txt--green
                | El enunciado de cada pregunta debe contener máximo 35 palabras.
              li
                i.fas.fa-angle-right.txt--green
                | La opción de respuesta debe contener máximo 20 palabras.
              li
                i.fas.fa-angle-right.txt--green
                | El mensaje final de la actividad debe contener máximo 25 palabras.
              li
                i.fas.fa-angle-right.txt--green
                | La retroalimentación de cada pregunta debe contener máximo 20 palabras.

              li
                i.fas.fa-angle-right.txt--green
                | Se permite un máximo de 12 preguntas.

    separador

    #t_5_2
    
    .titulo-segundo.color-acento-contenido
      h2 5.2 Relación de términos

    .tarjeta.clr--gris.p-5.mb-4
      .row.justify-content-around.align-items-center
        .col-8.col-lg-5.mb-4.mb-md-0
          img(src="@/assets/curso/temas/actividad/actividad_01.png").mb-3

        .col-md.col-lg-6
          h3 Ejemplo de relación de términos
          p.mb-4 #[strong Arrastrar y soltar coincidencias.] De acuerdo a la definición planteada en la columna izquierda, arrastre cada término al lugar que considere correcto de la columna derecha.
          a.boton.boton--b(:href="obtenerLink('/actividades/AD1/index.html')" target="_blank")
            span Realizar
            i.fas.fa-puzzle-piece

    .row
      .col-lg-12.order-2.order-lg-1
        TabsA.color-acento-botones
          .tarjeta.clr--gris.p-4(titulo="Requerimientos")
            ul.lista-ul.mb-0
              li
                i.fas.fa-angle-right.txt--green
                | Las indicaciones, el mensaje de correcto e incorrecto debe estar la redacción en segunda persona.
              li
                i.fas.fa-angle-right.txt--green
                | Al final de la actividad se muestra una retroalimentación de felicitación si logra el 70% de respuestas correctas o retroalimentación de mejora si es inferior a este porcentaje.
              li
                i.fas.fa-angle-right.txt--green
                | Se permiten un máximo de 6 enunciados.
              li
                i.fas.fa-angle-right.txt--green
                | Cada enunciado debe contener máximo 20 palabras.
              li
                i.fas.fa-angle-right.txt--green
                | Cada término que se debe relacionar a un enunciado debe tener máximo 3 palabras.

    separador

    #t_5_3
    
    .titulo-segundo.color-acento-contenido
      h2 5.3 Completar frases

    .tarjeta.clr--gris.p-5.mb-4
      .row.justify-content-around.align-items-center
        .col-8.col-lg-5.mb-4.mb-md-0
          img(src="@/assets/curso/temas/actividad/actividad_03.png").mb-3

        .col-md.col-lg-6
          h3 Ejemplo #1  completar frases
          p.mb-4 #[strong Instrucciones.] Escuche los audios, complete los espacios en blanco de cada una de las frases y luego haga clic en el botón "Verificar respuesta"

          a.boton.boton--b(:href="obtenerLink('/actividades/AD3/index.html')" target="_blank")
            span Realizar
            i.fas.fa-puzzle-piece


    .tarjeta.clr--gris.p-5.mb-5
      .row.justify-content-around.align-items-center
        .col-8.col-lg-5.mb-4.mb-md-0
          img(src="@/assets/curso/temas/actividad/actividad_04.png").mb-3

        .col-md.col-lg-6
          h3 Ejemplo #2  completar frases
          p.mb-4 #[strong Instrucciones.] Complete los espacios en blanco de cada una de las frases y luego haga clic en el botón "Verificar respuesta".

          a.boton.boton--b(:href="obtenerLink('/actividades/AD4/index.html')" target="_blank")
            span Realizar
            i.fas.fa-puzzle-piece

    .row
      .col-lg-12.order-2.order-lg-1
        TabsA.color-acento-botones
          .tarjeta.clr--gris.p-4(titulo="Requerimientos")
            ul.lista-ul.mb-0
              li
                i.fas.fa-angle-right.txt--green
                | Las indicaciones, el mensaje de correcto e incorrecto debe estar la redacción en segunda persona.
              li
                i.fas.fa-angle-right.txt--green
                | Al final de la actividad se muestra una retroalimentación de felicitación si logra el 70% de respuestas correctas o retroalimentación de mejora si es inferior a este porcentaje.
              li
                i.fas.fa-angle-right.txt--green
                | Se deben resaltar en amarillo las palabras del enunciado que deben completarse. Tenga en cuenta que cada espacio debe contener una sola palabra.

              li
                i.fas.fa-angle-right.txt--green
                | Se permiten un máximo de 7 enunciados.

              li
                i.fas.fa-angle-right.txt--green
                | Cada enunciado debe contener máximo 20 palabras.
              li
                i.fas.fa-angle-right.txt--green
                | Cada término que se debe escribir en el espacio en blanco debe tener máximo 1 sola palabra.

    separador
    
    #t_5_4

    .titulo-segundo.color-acento-contenido
      h2 5.4 Diálogos (Relación de términos en un diálogo)

    Dialogo.color-primario(:dialogo="dialogo")
      template(#nombre-actividad) Arrastrar y Soltar
      template(#titulo-actividad) Greeting the doctor. / Saludando al doctor.
      template(#descripcion-actividad) Escuche los audios y complete los espacios en blanco de cada una de las frases arrastrando el término correcto.
    .row.justify-content-end.mb-2.me-3
      .col-auto
        a.boton.color-primario.b--rad(:href="obtenerLink('/downloads/Dialogo.txt')" target="_blank" type="application/pdf")
          span Ver código fuente

</template>

<script>
export default {
  name: 'Tema5',
  data() {
    return {
      dialogo: {
        personajes: [
          {
            nombre: 'Doctor',
            img: require('@/assets/curso/temas/doctor.svg'),
          },
          {
            nombre: 'Jonathan',
            img: require('@/assets/curso/temas/jonathan.svg'),
          },
        ],
        dialogo: [
          {
            personaje: 'Jonathan',
            textoIng: 'Hello, Doctor. How are ***?',
            textoEsp: 'Hola, doctor. ¿Cómo estás?',
            audio: require('@/assets/audio/1.mp3'),
            palabra: 'you',
          },
          {
            personaje: 'Doctor',
            textoIng: 'Good *** Jonathan.',
            textoEsp: 'Buenos días Jonathan .',
            audio: require('@/assets/audio/2.wav'),
            palabra: 'morning',
          },
          {
            personaje: 'Doctor',
            textoIng: 'I am ***. How are you doing?.',
            textoEsp: 'Estoy bien, ¿cómo estás?',
            audio: require('@/assets/audio/3.wav'),
            palabra: 'great',
          },
          {
            personaje: 'Jonathan',
            textoIng: 'I&#8217m doing very well. I&#8217m feeling better.',
            textoEsp: 'Estoy muy bien. Me siento mejor.',
            audio: require('@/assets/audio/4.mp3'),
          },
          {
            personaje: 'Doctor',
            textoIng: 'It was *** to see you! I am glad you feel better.',
            textoEsp: ' ¡Qué gusto verte! Me alegro de que te sientas mejor.',
            audio: require('@/assets/audio/5.wav'),
            palabra: 'nice',
          },
          {
            personaje: 'Jonathan',
            textoIng: ' Thank you Doctor. *** a great day! ',
            textoEsp: 'Gracias Doctor. ¡Qué tengas un lindo día! ',
            audio: require('@/assets/audio/6.mp3'),
            palabra: 'have',
          },
          {
            personaje: 'Doctor',
            textoIng: ' ***.',
            textoEsp: 'Adiós.',
            audio: require('@/assets/audio/7.wav'),
            palabra: ' Goodbye. ',
          },
        ],
      },
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.$aosRefresh()
    })
  },
  updated() {
    this.$aosRefresh()
  },
}
</script>

<style lang="sass">
.tarjeta-reproductor
  &--izquierda
    position: relative
    &__img
      width: 300px
      position: absolute
      height: 100%
      left: 0
      bottom: 0
      transform: translateX(-30%) translateY(0%)
  &--derecha
    position: relative
    &__img
      width: 300px
      margin: 0 auto
      position: absolute
      height: 100%
      right: 0
      bottom: 0
      transform: translateX(30%) translateY(10%)
.franja
  position: relative
  &:before
    content: ''
    position: absolute
    bottom: 0%
    left: 0
    width: 100%
    height: 35%
    background-color: #ffd947
    z-index: 0
  .content
    position: inherit
.slyder__btn
  background-color: $color-acento-contenido
  i
    color: white !important
</style>

<style lang="sass"></style>
