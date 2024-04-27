// ignore_for_file: avoid_print
import 'package:flutter/widgets.dart';

//----------------SIN IMPLEMENTAR INTERFACE SEGREGATION-------------------
// abstract class PersonalClinica {
//   void atenderPaciente() {}
//   void gestionarCitas() {}
//   void limpiarClinica() {}
//   void brindarAtencion() {}
// }

// class MedicoImpl implements PersonalClinica {
//   @override
//   void atenderPaciente() {
//     print('Médico atendiendo al paciente...');
//   }
// }
// class AdministrativoImpl implements PersonalClinica {
//   @override
//   void gestionarCitas() {
//     print('Personal administrativo gestionando citas...');
//   }
// }
// class LimpiezaImpl implements PersonalClinica {
//   @override
//   void limpiarClinica() {
//     print('Personal de limpieza limpiando la clínica...');
//   }
// }
// class SecretariadoImpl implements PersonalClinica {
//   @override
//   void brindarAtencion() {
//     print('Personal de atención al paciente brindando atención...');
//   }
// }



// ---------------------------IMPLEMENTANDO INTERFACE SEGREGATION-------------------------------

class AtenderPaciente {
  void atenderPaciente() {
    print('Médico atendiendo al paciente...');
  }
}

class GestionarCitas {
  void gestionarCitas() {
    print('Personal administrativo gestionando citas...');
  }
}

class LimpiarClinica {
  void limpiarClinica() {
    print('Personal de limpieza limpiando la clínica...');
  }
}

class BrindarAtencion {
  void brindarAtencion() {
    print('Personal de atención al paciente brindando atención...');
  }
}

// Implementaciones concretas de las clases abstractas

class MedicoImpl2 {
  final AtenderPaciente atenderPacienteImpl = AtenderPaciente();

  void atenderPaciente() {
    atenderPacienteImpl.atenderPaciente();
  }
}

class AdministrativoImpl2 {
  final GestionarCitas gestionarCitasImpl = GestionarCitas();

  void gestionarCitas() {
    gestionarCitasImpl.gestionarCitas();
  }
}

class LimpiezaImpl2 {
  final LimpiarClinica limpiarClinicaImpl = LimpiarClinica();

  void limpiarClinica() {
    limpiarClinicaImpl.limpiarClinica();
  }
}

class SecretariadoImpl2 {
  final BrindarAtencion brindarAtencionImpl = BrindarAtencion();

  void brindarAtencion() {
    brindarAtencionImpl.brindarAtencion();
  }
}

class InterfaceSegregation extends StatelessWidget {
  final MedicoImpl2 medico = MedicoImpl2();
  final AdministrativoImpl2 administrativo = AdministrativoImpl2();
  final LimpiezaImpl2 limpieza = LimpiezaImpl2();
  final SecretariadoImpl2 secretariado = SecretariadoImpl2();

  InterfaceSegregation({super.key});

  @override
  Widget build(BuildContext context) {
    print('\n CON INTERFACE SEGREGATION');
    medico.atenderPaciente();
    administrativo.gestionarCitas();
    limpieza.limpiarClinica();
    secretariado.brindarAtencion();

    return Container();
  }
}
