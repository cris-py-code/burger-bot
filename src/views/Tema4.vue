<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido(data-aos="flip-up")
      .titulo-principal__numero
        span 4
      h1 Videos

    .row.justify-content-center.align-items-center.mb-5
      .col-lg-6
        figure
          img(src="@/assets/curso/temas/video/video.svg", alt="alt")
      .col-lg-6
        .crd.clr-paleYellow.p-4.mb-4
          p Cada tema relacionado en los contenidos de un recurso educativo digital puede incluir el desarrollo de los siguientes tipos de recursos audiovisuales: #[strong Spot animado, motion graphics y video clases.]

        p.mb-0 Se realizan #[strong videos temáticos] para reforzar la explicación de tema o concepto del recurso educativo digital y también #[strong videos de oferta] para hacerle publicidad al programa  que se está desarrollando.


    .row
      .col-lg-12.order-2.order-lg-1
        TabsA.color-acento-botones
          .tarjeta.clr--gris.p-4(titulo="Tipos de recursos audiovisuales")
            ul.lista-ul.mb-4
              li
                i.fas.fa-angle-right.txt--green
                | Spot animado, incluye la animación de personajes utilizando técnicas tradicionales de animación 2d.
              li
                i.fas.fa-angle-right.txt--green
                | Motion graphics, incluyen: animación de imágenes, recursos fotográficos y material pregrabado de audio y video.
              li
                i.fas.fa-angle-right.txt--green
                | Video clase, se genera a partir de un video el que el experto temático presenta pantalla con un tema específico o tutorial  y desde el equipo de producción se realizan las actividades de edición de video que incluye procesos como musicalización, limpieza de audio y adición de cortinillas intro/outro.
              li
                i.fas.fa-angle-right.txt--green
                | Live Action video en ambientes de aprendizaje y trabajo en exteriores, producción audiovisual generalmente realizada en un ambiente de aprendizaje donde están ubicadas los equipos, mesas de trabajo y/o maquinaria. Se requiere agendar con anticipación las jornadas de grabación.

            p.mb-0 #[strong Para la realización de los anteriores recursos audiovisuales se sugiere entregar solamente el guion con las indicaciones pertinentes y a partir del mismo el equipo de producción define el tipo de video a desarrollar.]

    separador

    figure
      .video
        iframe(width="560" height="315" src="https://www.youtube.com/embed/2L91WMqw96A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)
      figcaption.mt-2 Video: Leyenda del video
    .row.justify-content-end.mb-5.me-3
      .col-auto
        a.boton.color-acento-contenido.texto-blanco.b--rad(:href="obtenerLink('/downloads/video.txt')" target="_blank" type="application/pdf")
          span Ver código fuente 

</template>

<script>
export default {
  name: 'Tema4',
  data: () => ({
    // variables de vue
  }),
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

<style lang="sass"></style>
