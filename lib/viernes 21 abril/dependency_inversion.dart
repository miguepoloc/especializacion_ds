// ignore_for_file: avoid_print

//------------------SIN IMPLEMENTAR DEPENDENCY SEGREGATION---------------------------
// import 'package:flutter/material.dart';

// abstract class NotificationService {
//   void sendNotification(String message);
//   void cancelNotification(int id);
// }

// class PushNotificationService implements NotificationService {
//   @override
//   void sendNotification(String message) {
//     print('\nEnviando notificación push: $message');
//   }

//   @override
//   void cancelNotification(int id) {
//     print('\nCancelando notificación push con ID: $id');
//   }
// }

// class LocalNotificationService implements NotificationService {
//   @override
//   void sendNotification(String message) {
//     print('\nMostrando notificación local: $message');
//   }

//   @override
//   void cancelNotification(int id) {
//     print('\nCancelando notificación local con ID: $id');
//   }
// }

// class DependencyInversion extends StatelessWidget {
//   DependencyInversion({super.key});

//   @override
//   Widget build(BuildContext context) {
//     final pushNotification = PushNotificationService();
//     final localNotification = LocalNotificationService();

//     return MaterialApp(
//       home: Scaffold(
//         appBar: AppBar(
//           title: const Text('Dependency Inversion Example'),
//         ),
//         body: Center(
//           child: Column(
//             mainAxisAlignment: MainAxisAlignment.center,
//             children: [
//               ElevatedButton(
//                 onPressed: () {
//                   pushNotification.sendNotification('¡Nueva notificación push!');
//                 },
//                 child: const Text('Recibir Notificación Push'),
//               ),
//               ElevatedButton(
//                 onPressed: () {
//                   localNotification.sendNotification('¡Nueva notificación local!');
//                 },
//                 child: const Text('Recibir Notificación Local'),
//               ),
//               const SizedBox(height: 20),
//               ElevatedButton(
//                 onPressed: () {
//                   pushNotification.cancelNotification(1);
//                 },
//                 child: const Text('Cancelar Notificación Push con ID 1'),
//               ),
//               ElevatedButton(
//                 onPressed: () {
//                   localNotification.cancelNotification(1);
//                 },
//                 child: const Text('Cancelar Notificación Local con ID 1'),
//               ),
//             ],
//           ),
//         ),
//       ),
//     );
//   }
// }


//----------------------------------DEPENDENCY INVERSION IMPLEMENTADO-------------------------------------
// import 'package:flutter/material.dart';

// abstract class NotificationService {
//   void sendNotification(String message);
//   void cancelNotification(int id);
// }

// class PushNotificationService implements NotificationService {
//   @override
//   void sendNotification(String message) {
//     print('\nEnviando notificación push: $message');
//   }

//   @override
//   void cancelNotification(int id) {
//     print('\nCancelando notificación push con ID: $id');
//   }
// }

// class LocalNotificationService implements NotificationService {
//   @override
//   void sendNotification(String message) {
//     print('\nMostrando notificación local: $message');
//   }

//   @override
//   void cancelNotification(int id) {
//     print('\nCancelando notificación local con ID: $id');
//   }
// }

// class NotificationHandler {
//   final NotificationService _notificationService;

//   NotificationHandler(this._notificationService);

//   void handleNotification(String message) {
//     _notificationService.sendNotification(message);
//   }

//   void cancelNotification(int id) {
//     _notificationService.cancelNotification(id);
//   }
// }

// class DependencyInversion extends StatelessWidget {
//   final NotificationService pushNotification = PushNotificationService();
//   final NotificationService localNotification = LocalNotificationService();

//   DependencyInversion({super.key});

//   @override
//   Widget build(BuildContext context) {
//     final NotificationHandler pushNotificationHandler = NotificationHandler(pushNotification);
//     final NotificationHandler localNotificationHandler = NotificationHandler(localNotification); 
//     return MaterialApp(
//       home: Scaffold(
//         appBar: AppBar(
//           title: const Text('Dependency Inversion Example'),
//         ),
//         body: Center(
//           child: Column(
//             mainAxisAlignment: MainAxisAlignment.center,
//             children: [
//               ElevatedButton(
//                 onPressed: () {
//                   pushNotificationHandler.handleNotification('¡Nueva notificación push!');
//                 },
//                 child: const Text('Recibir Notificación Push'),
//               ),
//               ElevatedButton(
//                 onPressed: () {
//                   localNotificationHandler.handleNotification('¡Nueva notificación local!');
//                 },
//                 child: const Text('Recibir Notificación Local'),
//               ),
//               const SizedBox(height: 20),
//               ElevatedButton(
//                 onPressed: () {
//                   pushNotificationHandler.cancelNotification(1);
//                 },
//                 child: const Text('Cancelar Notificación Push con ID 1'),
//               ),
//               ElevatedButton(
//                 onPressed: () {
//                   localNotificationHandler.cancelNotification(1);
//                 },
//                 child: const Text('Cancelar Notificación Local con ID 1'),
//               ),
//             ],
//           ),
//         ),
//       ),
//     );
//   }
// }
